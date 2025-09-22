// https://leetcode.com/problems/implement-stack-using-queues
class MyStack {
private:
    std::queue<int> queue;
    int front;

public:
    MyStack() {
    }

    // O(1)
    void push(int x) {
        this->queue.push(x);
        this->front = x;
    }

    // O(n)
    int pop() {
        for (int i = 0; i < this->queue.size() - 1; i++) {
            this->front = this->queue.front();
            this->queue.push(this->queue.front());
            this->queue.pop();
        }
        int x = this->queue.front();
        this->queue.pop();
        return x;
    }

    // O(1)
    int top() {
        return this->front;
    }

    // O(1)
    bool empty() {
        return this->queue.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */

