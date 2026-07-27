#include <iostream>
#include <vector>
#include <utility>

class QuizResults {
public:
    explicit QuizResults(const std::vector<int>& scores) : scores_(scores) {}

    void partitionByThreshold(int threshold) {
        int i = 0;
        for (int j = 0; j < static_cast<int>(scores_.size()); ++j) {
            if (scores_[j] <= threshold) {
                std::swap(scores_[i], scores_[j]);
                ++i;
            }
        }
    }

    void print() const {
        for (int s : scores_) std::cout << s << " ";
        std::cout << std::endl;
    }

private:
    std::vector<int> scores_;
};

int main() {
    QuizResults results({45, 82, 60, 91, 33, 77});
    results.partitionByThreshold(60);
    results.print();
    return 0;
}