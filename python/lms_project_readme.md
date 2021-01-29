LMS(Library Mangement System) is a python based project designed using sqlite db.

The main features include:
1. A student cannot issue more than two copies of the same book
2. A student cannot issue more than two books
3. Admin password checker
4. A proper record log to see which book has been issued to whom

It has two portals:

1. Admin has to create an account(if first time user) and then login. all details of everything will be stored in the db. the admin can:
  1. Add/remove books
  2. Add/delete students from student list
  3. Can see who has taken which book
  4. Can update the no. of books available in the Library

2. Librarian can:
  1. Issue books
  2. Return books
  3. Can see which book is taken by which student
  4. Can see what books are taken by a particular student
