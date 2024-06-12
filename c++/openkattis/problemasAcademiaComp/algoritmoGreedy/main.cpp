
#include <algorithm>
#include <vector>
#include <iostream>

struct Event {
    int start;
    int end;
};

std::vector<Event> maxEvents(std::vector<Event>& events) {
    std::sort(events.begin(), events.end(), [](const Event& a, const Event& b) {
        return a.end < b.end;
    });

    std::vector<Event> selectedEvents;
    selectedEvents.push_back(events[0]);

    for (int i = 1; i < events.size(); ++i) {
        if (events[i].start >= selectedEvents.back().end) {
            selectedEvents.push_back(events[i]);
        }
    }

    return selectedEvents;
}

int main() {
    std::vector<Event> events = {{1, 3}, {2, 5}, {3, 9}, {6, 8}};
    auto selectedEvents = maxEvents(events);
    std::cout << "Selected events: \n";
    for (const auto& event : selectedEvents) {
        std::cout << "Start: " << event.start << ", End: " << event.end << "\n";
    }
    return 0;
}
