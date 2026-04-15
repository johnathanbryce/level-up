type PeopleType = { name: string; department: string };
type PeopleGrouped = Record<string, PeopleType[]>;

function groupBy(
  people: PeopleType[],
  keyName: keyof PeopleType,
): PeopleGrouped {
  const grouped = people.reduce<PeopleGrouped>(
    (accumulator, currentValue, currentIndex, array) => {
      let currKeyName = currentValue[keyName];

      // if the key doesn't exist on the acc yet, create it as an empty array
      if (!accumulator[currKeyName]) {
        accumulator[currKeyName] = [];
      }
      // then push
      accumulator[currKeyName].push(currentValue);
      return accumulator;
    },
    {},
  );

  console.log(grouped);
  return grouped;
}

const people = [
  { name: "Alice", department: "engineering" },
  { name: "Bob", department: "marketing" },
  { name: "Charlie", department: "engineering" },
  { name: "Diana", department: "marketing" },
  { name: "Eve", department: "design" },
];

groupBy(people, "department");
// → {
//   engineering: [{ name: "Alice", ... }, { name: "Charlie", ... }],
//   marketing: [{ name: "Bob", ... }, { name: "Diana", ... }],
//   design: [{ name: "Eve", ... }]
// }
