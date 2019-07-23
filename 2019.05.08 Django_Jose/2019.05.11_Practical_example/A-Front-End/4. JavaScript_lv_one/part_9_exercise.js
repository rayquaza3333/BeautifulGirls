first_name = prompt(" What is your First name?")
last_name = prompt(" What is your Last name?")
age = prompt(" What is your age?")
height = prompt(" What is your height in centimeter?")
pet_name = prompt(" What is your pet's name?")

if (
  first_name[0].toLowerCase()==last_name[0].toLowerCase()
  &&
  age > 20 && age < 30
  &&
  height >= 170
  &&
  pet_name[(pet_name.length - 1)].toLowerCase() == "y"
) {
  console.log("Congratualation")
}
