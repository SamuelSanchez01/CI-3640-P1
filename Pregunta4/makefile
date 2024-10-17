#Variables
CXX = g++
CXXFLAGS = -std=c++17 --coverage
LDFLAGS = --coverage

#Source file
SRC_FILE = quaternions.cpp
BUILD_DIR = build

# Targets
all: run-tests

$(BUILD_DIR)/quaternions: $(BUILD_DIR)/quaternions.o
	@mkdir -p $(BUILD_DIR)
	$(CXX) $(CXXFLAGS) -o $@ $^

$(BUILD_DIR)/quaternions.o: $(SRC_FILE)
	@mkdir -p $(BUILD_DIR)
	$(CXX) $(CXXFLAGS) -c -o $@ $<

# Phony targets
.PHONY: clean run-tests

clean:
	rm -rf $(BUILD_DIR) *.gcno *.gcda

run-tests: $(BUILD_DIR)/quaternions
	./$(BUILD_DIR)/quaternions