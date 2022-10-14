object Main extends App{

  def startStop[A] (l: List[A] ,start: Int, stop: Int): List[A] =
    l match {
      case Nil => Nil
      case x::xs =>
        if (start == 0 && stop == 0) Nil
        else if (start == 0) x :: startStop(xs,0,stop-1)
        else startStop(xs, start-1, stop-1)
    }

  println(startStop(List(1,2,3,4,5,6),1,4))

  def countChars (s:String): Map[Char,Int] = {
    def aux(l: List[Char], acc: Map[Char,Int]): Map[Char,Int] = {
      l match {
        case Nil => acc
        case x :: xs =>
          if (acc contains x) aux(xs,acc + (x -> (acc(x) + 1)))
          else aux(xs,acc + (x -> 1))
      }
    }
    aux(s.toList,Map())
  }

  println(countChars("MateiPopovici"))

  /*
  Write a function which takes a list of records first name, last name,
   CNP (encoded as tuples), and returns a list of the last names and ages
   of all females which are younger than the average of the entire list.
   E.g. [ (“Mary”, “2030694123456”), (“Anne”,“2121092123456”),
   (“Matei”, “5121202123456”),
   (“Maggie”, “2121078123456”)] yields [(“Mary”,19), (“Anne”,29)]. Maggie was born in '78, whereas Mary, Anne and Matei were born in '94, '92 and 2002, respectively.
   */

  def youngerThanAverage(l: List[(String,String)]): List[(String,Int)] = {
    def getAge(s:String):Int = {
      if (List('1','2') contains s(0)) (2022 - 1900 - s.slice(5,7).toInt)
      else if (List('5','6') contains s(0)) (2022 - 2000 - s.slice(5,7).toInt)
      else 0
    }
    // female gender = True
    def getGender(s:String):Boolean = List('2','6') contains s(0)
    // all females
    val res = l.filter(p => getGender(p._2))
    // average
    val avg: Float  = res.map(p => getAge(p._2)).reduce(_ + _) / res.size
    //final filter and age conversion
      res
        .filter(p => getAge(p._2) < avg)
        .map(p => (p._1, getAge(p._2)))
  }

  println(youngerThanAverage(List(("Mary",  "2030694123456"), ("Anne",  "2121092123456"), ("Matei", "5121202123456"), ("Maggie", "2121078123456"))))

  type Streets = Map[(Int,Char),Set[Int]]

  def readStreets(s: String): Streets = {
    def op(street: String, acc: Streets): Streets = {
      val x = street.split(' ')
      val src = x(0).toInt
      val color = x(1).head
      val dst = x(2).toInt
      if (acc contains (src,color)) acc + ((src,color) -> (acc((src,color)) + dst))
      else acc + ((src,color) -> Set(dst))
    }
    s.split('\n').foldRight(Map(): Streets)(op)
  }

  val example = """0 r 1
                  |0 r 2
                  |0 g 1
                  |1 g 2
                  |1 b 3
                  |1 r 4
                  |4 g 1
                  |3 b 2
                  |2 r 2
                  |2 g 3""".stripMargin

  println(readStreets(example))

  def findDestination(start: Int, colors: String, streets: Streets): Set[Int] = {
    def op(crtNodes: Set[Int],color: Char): Set[Int] = {
      println(crtNodes)
      (for (node <- crtNodes) yield {
        if (streets contains(node, color)) {println(streets((node,color))); streets((node, color))}
        else Set()
      }).flatten
    }
      colors.toList.foldLeft(Set(start))(op)
  }

  println(findDestination(0,"rrg",readStreets(example)))


}
