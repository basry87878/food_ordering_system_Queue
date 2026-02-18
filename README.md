# 🍕 Multithreaded Food Ordering System

A Python implementation of the classic **Producer-Consumer problem** using multithreading and a custom Queue, simulating a real-world food ordering and serving workflow.

---

## 📌 Problem Statement

Design a food ordering system that runs two concurrent threads:

- **Place Order** — Produces food orders and inserts them into a queue every **0.5 seconds**
- **Serve Order** — Consumes and serves orders from the queue every **2 seconds**, starting **1 second** after the place order thread

This is a classic **Producer-Consumer** problem where `place_order` produces orders and `serve_order` consumes them using a shared `Queue`.

---

## 🚀 Features

- Custom `Queue` class built from scratch using a Python list
- Two concurrent threads managing order placement and serving
- Simulated real-world timing delays using `time.sleep()`
- Clean FIFO (First In, First Out) queue behaviour

---

## 🗂️ Project Structure

```
food-ordering-system/
│
├── food_order.py       # Main application file
└── README.md           # Project documentation
```

---

## 🧠 How It Works

```
Thread 1 (Place Order)          Queue            Thread 2 (Serve Order)
        |                         |                        |
  t=0s  |── enqueue("pizza") ──>  [pizza]                  |
  t=0.5s|── enqueue("samosa") ─> [samosa, pizza]           |
  t=1s  |── enqueue("pasta") ──> [pasta, samosa, pizza] ──>| dequeue() → "pizza"
  t=1.5s|── enqueue("biryani")─> [biryani, pasta, samosa]  |
  t=2s  |── enqueue("burger") ─> [burger, biryani, pasta]  |
  t=3s  |                        [burger, biryani]  ──────>| dequeue() → "samosa"
        ...                          ...                    ...
```

---

## ⚙️ Setup & Usage

### Prerequisites
- Python 3.x

### Run the program

```bash
git clone https://github.com/basry87878/food-ordering-system.git
cd food-ordering-system
python food_order.py
```

### Expected Output

```
Placing order: pizza
Placing order: samosa
Serving order: pizza
Placing order: pasta
Placing order: biryani
Placing order: burger
Serving order: samosa
Serving order: pasta
...
All orders processed!
```

---

## 🧩 Core Components

### `Queue` Class

| Method | Description |
|---|---|
| `enqueue(value)` | Inserts item at the front of the buffer |
| `dequeue()` | Removes and returns item from the back (FIFO) |
| `is_empty()` | Returns `True` if the queue has no items |
| `size()` | Returns the current number of items in the queue |

### Threads

| Thread | Function | Interval |
|---|---|---|
| `t1` | `place_orders(q)` | Every 0.5s |
| `t2` | `serve_orders(q)` | Every 2s (starts after 1s delay) |

---

## ⚠️ Known Limitations & Improvements

| Issue | Severity | Recommended Fix |
|---|---|---|
| No thread lock on Queue | 🔴 High | Add `threading.Lock()` to protect shared buffer |
| `serve_orders` may exit early if queue is temporarily empty | 🟠 Medium | Track total served count or use a sentinel value |
| Using `list.insert(0, ...)` is O(n) | 🟡 Low | Use `collections.deque` for O(1) operations |

### Thread-Safe Queue (Recommended)

```python
class Queue:
    def __init__(self):
        self.buffer = []
        self.lock = threading.Lock()

    def enqueue(self, value):
        with self.lock:
            self.buffer.insert(0, value)

    def dequeue(self):
        with self.lock:
            return self.buffer.pop()
```

> 💡 Alternatively, use Python's built-in [`queue.Queue`](https://docs.python.org/3/library/queue.html) which is thread-safe by design.

---

## 📚 Concepts Covered

- **Multithreading** in Python using the `threading` module
- **Producer-Consumer** design pattern
- **Queue** data structure (custom implementation)
- **Thread synchronisation** with `join()` and `sleep()`
- **Race conditions** and how to mitigate them with locks

---

## 📖 References

- [Python `threading` Documentation](https://docs.python.org/3/library/threading.html)
- [Python `queue` Documentation](https://docs.python.org/3/library/queue.html)
- [Producer-Consumer Problem – Wikipedia](https://en.wikipedia.org/wiki/Producer%E2%80%93consumer_problem)

---

## 👤 Author

**Basry**
- GitHub: [@basry87878](https://github.com/basry87878)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
