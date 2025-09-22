// https://leetcode.com/problems/implement-queue-using-stacks
class MyQueue {
private:
    std::stack<int> stackTopDown;
    std::stack<int> stackBottomUp;
    int front;

public:
    MyQueue() {
    }

    // O(n)
    void push(int x) {
        while (this->stackTopDown.size() > 0) {
            this->stackBottomUp.push(this->stackTopDown.top());
            this->stackTopDown.pop();
        }

        if (this->stackBottomUp.empty()) {
            this->front = x;
        }
        this->stackBottomUp.push(x);
    }

    // O(n)
    int pop() {
        while (this->stackBottomUp.size() > 0) {
            this->stackTopDown.push(this->stackBottomUp.top());
            this->stackBottomUp.pop();
        }

        int x = this->stackTopDown.top();
        this->stackTopDown.pop();
        if (this->stackTopDown.size() > 0) {
            this->front = this->stackTopDown.top();
        }
        return x;
    }

    // O(1)
    int peek() {
        return this->front;
    }

    // O(1)
    bool empty() {
        return this->stackTopDown.empty() && this->stackBottomUp.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */

