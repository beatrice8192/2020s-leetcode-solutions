// https://leetcode.com/problems/implement-stack-using-queues
class MyStack {
private:
    std::queue<int> queue;

public:
    MyStack() {
    }

    // O(n)
    void push(int x) {
        this->queue.push(x);
        for (int i = 0; i < this->queue.size() - 1; i++) {
            this->queue.push(this->queue.front());
            this->queue.pop();
        }
    }

    // O(1)
    int pop() {
        int tmp = this->queue.front();
        this->queue.pop();
        return tmp;
    }

    // O(1)
    int top() {
        return this->queue.front();
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

