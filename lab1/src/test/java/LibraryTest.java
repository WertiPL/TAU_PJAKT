
import org.example.*;

import org.junit.jupiter.api.Test;

import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

public class LibraryTest {
    @Test
    public void testCheckOutBook() {
        Library library = new Library();
        Book book = new Book("Jack Reacher", "Lee Child");
        Customer customer = new Customer("Wiktor");

        library.addBook(book);
        library.addCustomer(customer);

        assertTrue(library.checkOutBook(book, customer));//Type of assert use 1 not repeat
        assertTrue(book.isCheckedOut());//Type of assert use 1  repeat
    }

    @Test
    public void testReturnBook() {
        Library library = new Library();
        Book book = new Book("1984", "George Orwell");

        library.addBook(book);
        book.checkOut(); // Simulate book being checked out.

        library.returnBook(book);
        assertFalse(book.isCheckedOut());//Type of assert use 2 not repeat
    }

    @Test
    public void testInvalidCheckOut() {
        Library library = new Library();
        Book book = new Book("Ogniem i mieczem", "Henryk Siekiewicz");
        Customer customer = new Customer("Olaf");

        assertFalse(library.checkOutBook(book, customer)); // Should fail, book not in the library.
        assertFalse(book.isCheckedOut());//Type of assert use 2  repeat
    }

    @Test
    public void testCustomerName() {
        Customer customer = new Customer("Elżbieta");
        assertEquals("Elżbieta", customer.getName());//Type of assert use 3  not repeat
    }

    @Test
    public void testAddBookToLibrary() {
        Library library = new Library();
        Book book = new Book("The Catcher in the Rye", "J.D. Salinger");
        Customer customer = new Customer("JANEK");
        library.addBook(book);
        assertTrue(library.checkOutBook(book, customer)); // Book should be available to check out. //Type of assert use 1  repeat
    }
    @Test
    public void testBookTitleAndAuthor() {
        Book book = new Book("The Hobbit", "J.R.R. Tolkien");
        assertEquals("The Hobbit", book.getTitle());
        assertEquals("J.R.R. Tolkien", book.getAuthor());//Type of assert use 3  repeat
    }

    @Test
    public void testCustomerNameChange() {
        Customer customer = new Customer("Jan");
        assertEquals("Jan", customer.getName());//Type of assert use 3  repeat

        // Change the customer's name
        customer.setName("Julia");
        assertEquals("Julia", customer.getName());//Type of assert use 3  repeat
    }

    @Test
    public void testLibraryBookList() {
        Library library = new Library();
        Book book1 = new Book("Dune", "Frank Herbert");
        Book book2 = new Book("The Shining", "Stephen King");

        library.addBook(book1);
        library.addBook(book2);

        List<Book> books = library.getBooks();
        assertNotNull(books);//library has books //Type of assert use 4 not repeat
    }

    @Test
    public void testLibraryCustomerList() {
        Library library = new Library();

        // Create an empty Book array of the same type as library.getBooks()
        Book[] emptyBookArray = new Book[0];

        Customer customer1 = new Customer("Alice");
        Customer customer2 = new Customer("Bob");

        library.addCustomer(customer1);
        library.addCustomer(customer2);
        List<Customer> customers = library.getCustomers();
        assertNotNull(customers);

        assertArrayEquals(emptyBookArray, library.getBooks().toArray());//library do not have books //Type of assert use 5 not repeat
    }
    @Test
    public void testLibraryPatronListSize() {
        Library library = new Library();
        Customer patron1 = new Customer("Jan");
        Customer patron2 = new Customer("Mateusz");

        library.addCustomer(patron1);
        library.addCustomer(patron2);

        List<Customer> patrons = library.getCustomers();
        assertEquals(2, patrons.size());//Type of assert use 3  repeat
    }

}