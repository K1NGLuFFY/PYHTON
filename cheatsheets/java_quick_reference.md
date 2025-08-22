# Java Quick Reference Card

## 🚀 Setup & Run
```bash
# Compile
javac MyClass.java

# Run
java MyClass
```

## 📊 Data Types
| Type | Size | Example |
|------|------|---------|
| byte | 8-bit | `byte b = 100;` |
| short | 16-bit | `short s = 1000;` |
| int | 32-bit | `int i = 100000;` |
| long | 64-bit | `long l = 100000L;` |
| float | 32-bit | `float f = 3.14f;` |
| double | 64-bit | `double d = 3.14;` |
| char | 16-bit | `char c = 'A';` |
| boolean | 1-bit | `boolean b = true;` |

## 🔄 Loops
```java
// For loop
for (int i = 0; i < 10; i++) { }

// While loop
while (condition) { }

// Do-while
do { } while (condition);

// Enhanced for
for (String item : array) { }
```

## 📦 Arrays
```java
// Declaration
int[] arr = new int[5];
int[] arr2 = {1, 2, 3, 4, 5};

// Access
arr[0] = 10;
int first = arr[0];
```

## 🏗️ Class Structure
```java
public class MyClass {
    // Fields
    private int field;
    
    // Constructor
    public MyClass(int field) {
        this.field = field;
    }
    
    // Method
    public void method() {
        // code
    }
}
```

## 🎯 Object Creation
```java
MyClass obj = new MyClass(10);
obj.method();
```

## 🧵 String Methods
| Method | Description |
|--------|-------------|
| `length()` | String length |
| `charAt(i)` | Character at index |
| `substring(s, e)` | Substring |
| `toUpperCase()` | Uppercase |
| `toLowerCase()` | Lowercase |
| `equals(str)` | String comparison |
| `contains(str)` | Contains substring |
| `replace(a, b)` | Replace characters |
| `split(regex)` | Split string |

## 📋 Collections
```java
// ArrayList
import java.util.ArrayList;
ArrayList<String> list = new ArrayList<>();
list.add("item");
list.get(0);
list.remove(0);

// HashMap
import java.util.HashMap;
HashMap<String, Integer> map = new HashMap<>();
map.put("key", 1);
map.get("key");
```

## ⚠️ Exception Handling
```java
try {
    // risky code
} catch (Exception e) {
    // handle exception
} finally {
    // cleanup
}
```

## 📥 Input
```java
import java.util.Scanner;
Scanner sc = new Scanner(System.in);
String input = sc.nextLine();
int number = sc.nextInt();
sc.close();
```

## 🔍 Math Functions
| Function | Description |
|----------|-------------|
| `Math.max(a, b)` | Maximum |
| `Math.min(a, b)` | Minimum |
| `Math.sqrt(x)` | Square root |
| `Math.pow(a, b)` | Power |
| `Math.abs(x)` | Absolute value |
| `Math.random()` | Random 0-1 |
| `Math.round(x)` | Round |
| `Math.floor(x)` | Floor |
| `Math.ceil(x)` | Ceiling |

## 🎨 Formatting
```java
// Print
System.out.println("Hello");
System.out.print("Hello");

// Format
System.out.printf("Name: %s, Age: %d", name, age);
```

## 🏷️ Modifiers
| Modifier | Description |
|----------|-------------|
| `public` | Accessible everywhere |
| `private` | Accessible within class |
| `protected` | Accessible within package and subclasses |
| `default` | Accessible within package |
| `static` | Belongs to class |
| `final` | Cannot be changed |
| `abstract` | Must be implemented |

## 🔄 Inheritance
```java
class Parent {
    // parent class
}

class Child extends Parent {
    // child class
}
```

## 🎯 Interface
```java
interface MyInterface {
    void method();
}

class MyClass implements MyInterface {
    public void method() {
        // implementation
    }
}
```

## 🚀 Main Method
```java
public static void main(String[] args) {
    // program starts here
}
```

## 💡 Quick Tips
- Class name must match file name
- Java is case-sensitive
- Use `//` for single-line comments
- Use `/* */` for multi-line comments
- Always close Scanner with `sc.close()`
- Use `equals()` for string comparison, not `==`
