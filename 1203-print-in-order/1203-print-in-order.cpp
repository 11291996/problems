//use conditional variable 
class Foo {
    condition_variable cv; //conditional address 
    mutex mtx;
    int currentPrint;
public:
    Foo() {
        currentPrint=1;
    }

    void first(function<void()> printFirst) {
        unique_lock<mutex>lock(mtx); //initialize a lock
        currentPrint=2; //updates conditional variable 
        printFirst();
        cv.notify_all(); //broadcasting 
    } //c++ mutex unlocks as the function terminals 

    void second(function<void()> printSecond) {
        unique_lock<mutex>lock(mtx);
        cv.wait(lock,[&](){return currentPrint==2;}); //waits for the condition 
        currentPrint=3;
        printSecond();
        cv.notify_one();
    }

    void third(function<void()> printThird) {
        unique_lock<mutex>lock(mtx);
        cv.wait(lock,[&](){return currentPrint==3;}); //waits for the condition
        printThird();
    }
};