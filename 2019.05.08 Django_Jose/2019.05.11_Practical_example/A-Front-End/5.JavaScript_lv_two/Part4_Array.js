while (true) {
  var list=[]

  while (true){

        if (prompt("Do you want to start the roster web app? (y/n)") == "y"){
                var decision=prompt("Which command do you want to make? (add/remove/display/quit)");
               if (decision === "add"){
                  list.push(prompt("What name do you want to add?"));
                  continue
                }
               if (decision === "remove"){
                  list.pop(prompt("Which name do you want to remove?"));
                  continue
                }
               if (decision === "display"){
                  console.log(list);
                  continue
                }
               if (decision === "quit"){

                  break;

                }

          }
          break;

    }
  alert("Thank you for join us");
  break;
}
