package org.example;

import java.util.ArrayList;
import java.util.List;

public class Library {
    private List<Book> books;
    private List<Customer> Customers;

    public Library() {
        books = new ArrayList<>();
        Customers = new ArrayList<>();
    }

    public void addBook(Book book) {
        books.add(book);
    }

    public void addCustomer(Customer Customer) {
        Customers.add(Customer);
    }

    public boolean checkOutBook(Book book, Customer Customer) {
        if (book.isCheckedOut() || !books.contains(book)) {
            return false; // Book cannot be checked out.
        }

        book.checkOut();
        return true;
    }

    public void returnBook(Book book) {
        if (books.contains(book)) {
            book.returnBook();
        }
    }

    public List<Book> getBooks() {
        return books;
    }

    public void setBooks(List<Book> books) {
        this.books = books;
    }

    public List<Customer> getCustomers() {
        return Customers;
    }

    public void setCustomers(List<Customer> Customers) {
        this.Customers = Customers;
    }
}