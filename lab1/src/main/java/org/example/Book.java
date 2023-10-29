package org.example;

import java.util.ArrayList;
import java.util.List;

public class Book {
    private String title;
    private String author;
    private boolean checkedOut;

    public Book(String title, String author) {
        this.title = title;
        this.author = author;
        this.checkedOut = false;
    }

    public String getTitle() {
        return title;
    }

    public String getAuthor() {
        return author;
    }

    public boolean isCheckedOut() {
        return checkedOut;
    }

    public void checkOut() {
        if (!checkedOut) {
            checkedOut = true;
        }
    }

    public void returnBook() {
        if (checkedOut) {
            checkedOut = false;
        }
    }
}





