# Java Basics Tutorial

## What is Java?
Java is a high-level, object-oriented programming language developed by Sun Microsystems (now Oracle) in 1995. It's platform-independent ("write once, run anywhere") and widely used for web, mobile, and enterprise applications.

## Java Fundamentals

### 1. Basic Structure
```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

### 2. Variables and Data Types

#### Primitive Data Types:
- **byte**: 8-bit integer (-128 to 127)
- **short**: 16-bit integer (-32,768 to 32,767)
- **int**: 32-bit integer (-2.1B to 2.1B)
- **long**: 64-bit integer
- **float**: 32-bit floating point
- **double**: 64-bit floating point
- **char**: single character
- **boolean**: true/false

#### Example:
```java
int age = 25;
double price = 19.99;
char grade = 'A';
boolean isActive = true;
```

### 3. Operators

#### Arithmetic:
```java
+  -  *  /  %  ++  --
```

#### Comparison:
```java
==  !=  >  <  >=  <=
```

#### Logical:
```java
&&  ||  !
```

### 4. Control Flow

#### If-Else Statements:
```java
if (condition) {
    // code
} else if (condition) {
    // code
} else {
    // code
}
```

#### Switch Statement:
```java
switch (variable) {
    case value1:
        // code
        break;
    case value2:
        // code
        break;
    default:
        // code
}
```

#### Loops:
```java
// For loop
for (int i = 0; i < 10; i++) {
    // code
}

// While loop
while (condition) {
    // code
}

// Do-while loop
do {
    // code
} while (condition);
```

### 5. Arrays
```java
// Declaration
int[] numbers = new int[5];
int[] values = {1, 2, 3, 4, 5};

// Access
numbers[0] = 10;
int first = values[0];
```

### 6. Methods
```java
public static int add(int a, int b) {
    return a + b;
}

// Usage
int result = add(5, 3);
```

### 7. Classes and Objects

#### Class Definition:
```java
public class Car {
    // Fields
    String brand;
    int year;
    
    // Constructor
    public Car(String brand, int year) {
        this.brand = brand;
        this.year = year;
    }
    
    // Method
    public void start() {
        System.out.println("Car started!");
    }
}
```

#### Object Creation:
```java
Car myCar = new Car("Toyota", 2022);
myCar.start();
```

### 8. String Operations
```java
String name = "Java";
int length = name.length();
String upper = name.toUpperCase();
String lower = name.toLowerCase();
boolean contains = name.contains("av");
String replaced = name.replace("J", "H");
```

### 9. Exception Handling
```java
try {
    // risky code
    int result = 10 / 0;
} catch (ArithmeticException e) {
    System.out.println("Cannot divide by zero!");
} finally {
    // cleanup code
}
```

### 10. Input/Output
```java
import java.util.Scanner;

Scanner scanner = new Scanner(System.in);
System.out.print("Enter your name: ");
String name = scanner.nextLine();
System.out.println("Hello, " + name + "!");
scanner.close();
```

## Object-Oriented Programming Concepts

### 1. Encapsulation
```java
public class Person {
    private String name;  // private = restricted access
    
    // Getter
    public String getName() {
        return name;
    }
    
    // Setter
    public void setName(String newName) {
        name = newName;
    }
}
```

### 2. Inheritance
```java
class Animal {
    public void eat() {
        System.out.println("Animal eats");
    }
}

class Dog extends Animal {
    public void bark() {
        System.out.println("Dog barks");
    }
}
```

### 3. Polymorphism
```java
class Animal {
    public void makeSound() {
        System.out.println("Animal sound");
    }
}

class Dog extends Animal {
    @Override
    public void makeSound() {
        System.out.println("Dog barks");
    }
}
```

### 4. Abstraction
```java
abstract class Shape {
    abstract double calculateArea();
}

class Circle extends Shape {
    double radius;
    
    @Override
    double calculateArea() {
        return Math.PI * radius * radius;
    }
}
```

## Common Java Libraries

### 1. ArrayList
```java
import java.util.ArrayList;

ArrayList<String> list = new ArrayList<>();
list.add("Apple");
list.add("Banana");
list.remove(0);
```

### 2. HashMap
```java
import java.util.HashMap;

HashMap<String, Integer> map = new HashMap<>();
map.put("John", 25);
map.get("John");
```

### 3. Math Class
```java
int max = Math.max(5, 10);
double sqrt = Math.sqrt(16);
double random = Math.random();
```

## Best Practices
1. Use meaningful variable names
2. Follow camelCase naming convention
3. Always close resources (use try-with-resources)
4. Use proper exception handling
5. Write clear comments
6. Follow single responsibility principle
7. Understand that String is immutable
