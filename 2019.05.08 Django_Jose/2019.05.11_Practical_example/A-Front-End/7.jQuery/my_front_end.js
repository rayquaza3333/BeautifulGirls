var player_1 = prompt("Player One: Enter Your Name, you will be Blue");
var player_1_Color = 'rgb(86, 151, 255)';

var player_2 = prompt('Player Two: Enter Your Name, you will be Red');
var player_2_Color = 'rgb(237, 45, 73)';

var game_on =  true;
var table = $('table tr');


 function report_Win(row_Num,col_Num,win_Style){
   alert(current_Name + ': You won starting at this row: ' + row_Num +'; col: ' + col_Num + " in a " +win_Style );
 }

// Change the color of a button

function change_Color(row_Index,col_Index,color){
  return table.eq(row_Index).find('td').eq(col_Index).find('button').css('background-color',color);
}

// Report Back to current color of a button
function return_Color(row_Index,col_Index){
  return table.eq(row_Index).find('td').eq(col_Index).find('button').css('background-color');
}

// Take in column index, returns the bottom row that is still gray
function check_Bottom(col_Index){
  for (var row = 5; row > -1; row --) {
    var color_Return = return_Color(row,col_Index);
    if (color_Return === "rgb(128, 128, 128)"){
          return row;
    }
  }
}

// Check to see if 4 inputs are the same color
function color_Match_Check(one,two,three,four){
  return (one === two && two === three && three === four  && one !== "rgb(128, 128, 128)" && one !== undefined );
}

// Check for Horizontal Wins

function win_check_Horizontal(){
  for (var row = 0; row <= 5; row ++){
    for (var col = 0; col <= 3; col++){
      if (color_Match_Check(return_Color(row,col),return_Color(row,col+1),return_Color(row,col+2),return_Color(row,col+3),)) {
        report_Win(row,col,"Horizontal");
        return true;
      }
    }
  }
}
// Check for Vertical  Wins

function win_Check_Vertical(){
  for (var col = 0; col <= 6; col++){
    for (var row = 5; row >= 3; row--){
      if (color_Match_Check(return_Color(row,col),return_Color(row-1,col),return_Color(row-2,col),return_Color(row-3,col),)) {
        report_Win(row,col,"Horizontal");
        return true;
      }
    }
  }
}

// Check for Vertical  Wins

function win_check_Diagonal(){
  for (var col = 0; col <= 6; col++){
    for (var row = 0; row <=5 ; row ++){
      if (color_Match_Check(return_Color(row+1,col+1),return_Color(row+2,col+2),return_Color(row+3,col+3),return_Color(row+4,col+4),)) {
        report_Win(row,col,"Diagonal");
        return true;
      }
      else if (color_Match_Check(return_Color(row+1,col-1),return_Color(row+2,col-2),return_Color(row+3,col-3),return_Color(row+4,col-4),)) {
        report_Win(row,col,"Diagonal");
        return true;
      }
    }
  }
}

//Game End

function game_End(winningPlayer){
  $('h3').fadeOut('fast');
  $('h2').fadeOut('fast');
  $('h1').text(winningPlayer + " has Won! Refresh your browser to play again!")
}

// Start with Player One

var current_Player = 1
var current_Name = player_1
var current_Color = player_1_Color

$('h3').text(player_1+": it is your turn, please pick a column to drop your blue chip.");


$('.board button').on('click',function() {

  // Recognize what column was chosen
  var col = $(this).closest("td").index();
      // Let's explain a bit. Firstly, we cannot expect an (row x col) indexing in JAvaScript
      // (I did cause I thought it must had been for table)
      // IN JavaScript, there's only index of a element in its parent element.
      // And index of that parent <tr> element is index of itself in the parent <table>, Which is ROW_INDEX we are looking for.
      // So. it mean any <td> element will have index of itself in parent <tr> element. Which is COL_IDEX we are looking for.

  // Get back bottom available row to change
  var bot_Avai = check_Bottom(col);
  // Drop the chip in that column at the bottomAvail Row
  change_Color(bot_Avai,col,current_Color);


  // Check for a win or a tie.
  if (win_check_Diagonal() || win_check_Horizontal() || win_Check_Vertical() ) {
    game_End(current_Name);
  }

  // *debug block
  // console.log(bot_Avai);
  // console.log(col);
  // console.log("It's ok till here");

    // If no win or tie, continue to next player
    current_Player = current_Player* -1;

  // Re-Check who the current Player is.

  if (current_Player ===1){
    current_Name = player_1;
    current_Color = player_1_Color;
    $('h3').text(current_Name + ": It's your turn, plea pick a column to drop the blue chip.")
      console.log("Change to one ran");
  }else {
      current_Name = player_2;
      current_Color = player_2_Color;
      $('h3').text(current_Name + ": It's your turn, plea pick a column to drop the blue chip.")
        console.log("Change to two ran");
  }

})
