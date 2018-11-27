import breeze.linalg._
import org.apache.spark.{SparkConf, SparkContext}

object Recommend_restaurant {

  def calculateCosine( v1:DenseVector[Double], v2:DenseVector[Double]): Double= {
  var dot_pro =   v1 :* v2
    var v1_sq = v1 :* v1
    var v2_sq = v2 :* v2
    var sqrt1 =  math.sqrt(sum(v1_sq))
    var sqrt2 = math.sqrt(sum(v2_sq))
    if (sqrt1 < 0.000001 || sqrt2 < 0.000001) return 0
    return  sum(dot_pro) /  sqrt1  / sqrt2
  }

    def main(args: Array[String]): Unit = {

    val conf = new SparkConf()
    conf.setAppName("hw4")
    conf.setMaster("local[2]")
    val sc = new SparkContext(conf)

    val reviews = sc.textFile(args(0))
    //val review_list = reviews.collect()
    val vectors = reviews.map(line=>{
      var eles = line.split(" ")
      var oneVec = DenseVector.zeros[Double](7)
      oneVec(0) = eles(2).toDouble
      oneVec(1) = eles(3).toDouble
      oneVec(2) = eles(4).toDouble
      oneVec(3) = eles(5).toDouble
      oneVec(4) = eles(6).toDouble
      oneVec(5) = eles(7).toDouble
      oneVec(6) = eles(8).toDouble
      (eles(0), eles(1), oneVec)
    })

    var user_profiles = vectors.map(line=>{
      (line._1, line._3)
    }).reduceByKey((x, y)=>x+y).collectAsMap()

//    var userCnt = user_profiles.count()

    var item_profiles = vectors.map(line=>{
      (line._2, line._3)
    }).reduceByKey((x, y)=>x+y).collectAsMap()

//    var itemCnt = item_profiles.count()


    val test_data = sc.textFile(args(1))
    val test_analysis = test_data.map(line=>{
      var lines = line.split(" ")
      (lines(0), (lines(1), lines(2).toDouble))
    })

      val total_cnt = test_analysis.count()
     // println(test_analysis.count())
    /*
      test_analysis.groupByKey().map(line=>{
      var restaurantList = line._2.toList
      println(line._1)
      println(restaurantList.size)
      for (x <- restaurantList){
        if (user_profiles.contains(line._1) && item_profiles.contains(x._1)) {
          var cosval = calculateCosine(user_profiles(line._1), item_profiles(x._1))
          println(line._1 + " " + x._1 + " " + " cos:" + cosval.toString + " rate:" + x._2)
        }
      }
    })
      */
      var threshold = 0.3
     var recommends = test_analysis.map(line=>{
        var cosval =0.0
          if (user_profiles.contains(line._1) && item_profiles.contains(line._2._1)) {
            cosval = calculateCosine(user_profiles(line._1), item_profiles(line._2._1))
       //     println(line._1 + " " + line._2._1 + " " + " cos:" + cosval.toString + " rate:" + line._2._2)
          }
       // 0.3, 0.4, 0.5, 0.6
       if (cosval> threshold) {
         (line._1, line._2._1, 1)
       }else {
         (line._1, line._2._1, 0)
       }
      })
  }
}
