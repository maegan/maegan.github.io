import { useEffect, useState } from "react";
import { robots } from "./robot";
import CardList from "./CardList";
import SearchBox from "./SearchBox";

const FunctionalApp = () => {
  const [robotList, setRobots] = useState(robots);
  // use effect triggers when the page mounts or when a component is update.
  //the second parameter, the empty array, tells the function which components updating should trigger the callback
  // giving an empty array makes the callback only run when the page first mounts
  useEffect(() => {
    console.log("On Component Mount");
    fetch("https://jsonplaceholder.typicode.com/users")
      .then((response) => response.json())
      .then((users) => setRobots(users));
  }, []);

  let onSearchChange = (event) => {
    const copy = [...robots];
    const filteredCopy = copy.filter((robot) => {
      return robot.name
        .toLowerCase()
        .includes(event.target.value.toLowerCase());
    });
    setRobots(filteredCopy);
  };

  return (
    <div className="tc">
      <h3>Robot Friends</h3>
      <SearchBox searchChange={onSearchChange} />
      <CardList robots={robotList} />
    </div>
  );
};

export default FunctionalApp;
