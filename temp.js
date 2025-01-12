class Task {
  constructor(name) {
    this.name = name;
  }

  async run() {
    if (this.name === "Task 1") {
      return "Running Task 1";
    } else {
      return "Running other task";
    }
  }
}

const task1 = new Task("Task 1");
task1.run().then(result => console.log(result));

const check = true ? "Yes" : "No";
console.log(check);
