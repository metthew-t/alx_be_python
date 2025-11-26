import java.util.concurrent.*;
import java.util.concurrent.locks.*;

public class MultithreadingDemo {
    public static void main(String[] args) throws InterruptedException {
        // Using traditional synchronization
        SharedBuffer buffer = new SharedBuffer();
        
        // Create producers and consumers
        Thread producer1 = new Thread(new Producer(buffer, "Producer-1"));
        Thread producer2 = new Thread(new Producer(buffer, "Producer-2"));
        Consumer consumer1 = new Consumer(buffer, "Consumer-1");
        Consumer consumer2 = new Consumer(buffer, "Consumer-2");
        
        System.out.println("=== Starting Traditional Synchronization ===");
        producer1.start();
        producer2.start();
        consumer1.start();
        consumer2.start();
        
        // Wait for completion
        producer1.join();
        producer2.join();
        consumer1.join();
        consumer2.join();
        
        System.out.println("\n=== Starting Thread Pool Example ===");
        
        // Using Thread Pool (ExecutorService)
        ExecutorService executor = Executors.newFixedThreadPool(4);
        SharedBufferWithLock bufferWithLock = new SharedBufferWithLock();
        
        // Submit tasks to thread pool
        executor.execute(new Producer(bufferWithLock, "Pool-Producer-1"));
        executor.execute(new Producer(bufferWithLock, "Pool-Producer-2"));
        executor.execute(() -> {
            // Lambda expression for Runnable
            try {
                for (int i = 1; i <= 3; i++) {
                    String item = bufferWithLock.consume();
                    System.out.println("Pool-Consumer consumed: " + item);
                    Thread.sleep(100);
                }
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });
        
        // Shutdown executor
        executor.shutdown();
        executor.awaitTermination(5, TimeUnit.SECONDS);
        
        System.out.println("=== All tasks completed ===");
        
        // Demonstrate thread states and priorities
        System.out.println("\n=== Thread States and Priorities ===");
        Thread demoThread = new Thread(() -> {
            try {
                System.out.println("Demo thread running with priority: " + 
                    Thread.currentThread().getPriority());
                Thread.sleep(500);
                System.out.println("Demo thread finished");
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });
        
        demoThread.setName("Demo-Thread");
        demoThread.setPriority(Thread.MAX_PRIORITY);
        System.out.println("Thread state before start: " + demoThread.getState());
        demoThread.start();
        System.out.println("Thread state after start: " + demoThread.getState());
        demoThread.join();
        System.out.println("Thread state after completion: " + demoThread.getState());
    }
}

// 1. Using Runnable interface
class Producer implements Runnable {
    private SharedBuffer buffer;
    private String name;
    
    public Producer(SharedBuffer buffer, String name) {
        this.buffer = buffer;
        this.name = name;
    }
    
    public void run() {
        try {
            for (int i = 1; i <= 5; i++) {
                buffer.produce("Item-" + i);
                System.out.println(name + " produced: Item-" + i);
                Thread.sleep(100); // Simulate work
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}

// 2. Using Thread class extension
class Consumer extends Thread {
    private SharedBuffer buffer;
    private String name;
    
    public Consumer(SharedBuffer buffer, String name) {
        this.buffer = buffer;
        this.name = name;
    }
    
    public void run() {
        try {
            for (int i = 1; i <= 5; i++) {
                String item = buffer.consume();
                System.out.println(name + " consumed: " + item);
                Thread.sleep(150); // Simulate work
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}

// Shared resource with synchronization
class SharedBuffer {
    private final String[] buffer = new String[3];
    private int count = 0, putIndex = 0, takeIndex = 0;
    
    // Synchronized method example
    public synchronized void produce(String item) throws InterruptedException {
        while (count == buffer.length) {
            System.out.println("Buffer full, producer waiting...");
            wait(); // Thread communication - wait
        }
        
        buffer[putIndex] = item;
        putIndex = (putIndex + 1) % buffer.length;
        count++;
        
        notifyAll(); // Thread communication - notify waiting consumers
    }
    
    // Synchronized method example
    public synchronized String consume() throws InterruptedException {
        while (count == 0) {
            System.out.println("Buffer empty, consumer waiting...");
            wait(); // Thread communication - wait
        }
        
        String item = buffer[takeIndex];
        takeIndex = (takeIndex + 1) % buffer.length;
        count--;
        
        notifyAll(); // Thread communication - notify waiting producers
        return item;
    }
}

// Alternative using Lock and Condition
class SharedBufferWithLock {
    private final String[] buffer = new String[3];
    private int count = 0, putIndex = 0, takeIndex = 0;
    private final Lock lock = new ReentrantLock();
    private final Condition notFull = lock.newCondition();
    private final Condition notEmpty = lock.newCondition();
    
    public void produce(String item) throws InterruptedException {
        lock.lock();
        try {
            while (count == buffer.length) {
                System.out.println("Buffer full (Lock), producer waiting...");
                notFull.await(); // Using Condition
            }
            
            buffer[putIndex] = item;
            putIndex = (putIndex + 1) % buffer.length;
            count++;
            
            notEmpty.signalAll(); // Using Condition
        } finally {
            lock.unlock();
        }
    }
    
    public String consume() throws InterruptedException {
        lock.lock();
        try {
            while (count == 0) {
                System.out.println("Buffer empty (Lock), consumer waiting...");
                notEmpty.await(); // Using Condition
            }
            
            String item = buffer[takeIndex];
            takeIndex = (takeIndex + 1) % buffer.length;
            count--;
            
            notFull.signalAll(); // Using Condition
            return item;
        } finally {
            lock.unlock();
        }
    }
}