

# Data Structures

## Arrays

### Creating a BookShelf

Standing in my living room and looking around, I see books lying all over the place, some on the shelf, some on the ground in the corner of the room,
and even one or two sitting on the sofa.

I decide to finally clean up this mess and gather all of my books together, storing them neatly on a shelf which I designate exclusively for books; 
I'll never store my shoes on that shelf alongside the books, for example.

To declare the exclusivity of this shelf, I call it the "bookshelf" and label it for books only.
Of course, the shelf has a specific length which means that I can only store a certain number of books on it.
Let's say this shelf can store a maximum of 100 books, and every book takes up equal space on the shelf.

Finally, I want to ensure that guests don't rearrange the order that I've set the books on the shelf, so 
I also numbered each book from 1 to 100.

Inspired, my mind then wanders to my e-book collection, and how great it would be to code a software application that
works just like the book shelf; a virtual book shelf!
So, I wonder what is a suitable coding construct for this purpose?
 
That coding construct is known as an Array.

### What are Arrays 

Just like my physical book shelf, where all books are stored together in one place within the living room,
Arrays store their items together in one place within computer memory, this is known as contiguous memory allocation.

Arrays also provide order to their items, indexing each item from 0 to N, 
N being the coder's choice of the maximum number of items that this array can store;
just like my physical bookshelf can only store up to 100 books.

When I want to read a book, I look up the index and take it from the shelf.
Then when I'm finished reading it, I place it back on the shelf in the exact same place.

My virtual bookshelf will work like this too, except I never have to return the book to the shelf!
Isn't that great? I'll never have to clean up my e-books! 

Arrays do require the coder to specify the index where an item should be stored, this is called insertion,
as an item is being inserted into the array as a specific index location.

Anytime we reference a book from the virtual bookshelf, it never really leaves the shelf.
How? well that's just some virtual magic ;)

### Replacing Array Items

My friend, while browsing the books on my shelf, asks if he can borrow one of them in exchange for one of his that I'd like to read.
I take one book off my shelf and replace it with his book.

My virtual bookshelf array can handle this too, I simply insert a new book item at a specific index and this 
automatically replaces any existing book already in that index.  

### Inserting and Shifting Existing Items

I want to keep alphabetical order, so when adding a new book with a title beginning with 'B'
I'll shift the existing books with titles 'C' and above to the right to make room.

By the way, a book with a title beginning with 'Z' would be much easiser as I can simply add it to the end of the shelf, 
if there's space.

### Coding the Virtual Bookshelf and Examples

See "BookShelf.scala"
















