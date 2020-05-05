
object BookShelf extends App {

  // Create some books.
  // Imagine books are Strings for simplicity.
  var book1 = "A gentleman in Moscow"
  var book2 = "All Adults Here"
  var book3 = "Midnight Sun"
  var book4 = "Ulysses"
  var book5 = "Where the Crawdads Sing"

  // Create the virtual bookshelf using an Array.
  // It can hold 6 books.
  var bookShelf = new Array[String](6)

  println("How many books can be stored here?")
  println(bookShelf.length)

  // Add books to the shelf.
  // Remember array indexing begins at 0.
  bookShelf(0) = book1
  bookShelf(1) = book2
  bookShelf(2) = book3
  bookShelf(3) = book4
  bookShelf(4) = book5

  println("Show me what's on the shelf.")
  printBookShelfContents()

  /* Accessing array elements. */

  // I want to read...
  var myChoice = bookShelf(4)

  println("Show me my chosen book.")
  println(myChoice)

  // Remember the book never really leaves the shelf,
  // so I don't need to place it back.
  println("What's on the shelf at that index?")
  println(bookShelf(4))

  /* Inserting new elements. */

  // My friend borrows one from me in return for his book "Adventure Land".
  var bookForMyFriend = bookShelf(0)
  bookShelf(0) = "Adventure Land"

  println("Now what's on the shelf at that index?")
  println(bookShelf(0))

  // So my book is not on the shelf anymore,
  // but I still hold it in the variable bookForMyFriend.
  // This is like holding a real book in my hand, rather than on the shelf.
  println("Book for my friend: "+ bookForMyFriend)

  // My new book is called "Balancing Act" so I need to insert it at index 2
  // in place of "The Nest", but first I'll shift that existing book to the right.
  println("Show me what's on the shelf.")
  printBookShelfContents()

  // First, we will have to create space for a new element.
  // We do that by shifting each element one index to the right.
  // This will firstly move the last element at index 4, then 3, then finally 2,
  // since 2 is where the space should be.
  // We need to go backwards to avoid overwriting any elements.
  for (i <- 4 to (2,-1)) {
    bookShelf(i + 1) = bookShelf(i)
  }
  bookShelf(2) = "Balancing Act"

  println("Show me what's on the shelf.")
  printBookShelfContents()

  // -----------------
  /* Procedures used above. */

  def printBookShelfContents() {
    var index = 0
    do {
      println(index +" : "+ bookShelf(index))
      index = index+1
    } while ((index < bookShelf.length) && (bookShelf(index) != null))
  }
}
