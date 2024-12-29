 function clearDisplay(){
  document.getElementById('display').value = "";
  // This Line retrives the HTML element with the id of display using document.getElemenById
  // .value = ' '; sets the value of the display to an empty string (). this effectively clears anty texts
 }
 // used to display functions in  javavscrpit
  function deleteLast() {
     var display = document.getElementById('display');
     display.value = display.value.slice(0 , -1);
     // the let keyword declares a variable named display
     // document.getElemetById('display); retives theHTML element with the id of displlay
     // slice (0 , -1) remove the last chrachter from the string.slice (0,-1) work by taking
     // display.value = display.value.slice(0 , -1); updates the display to refklcet the new  
  }
   function appendNumber(number){
    var display = document.getElementById('display');
  // 
    display.value += number;
   }
    function appendOperator(operator) {
        var display = document.getElementById('display');
        var lastChar = display.value[display.value.length -1];

        if(display.value !== '' && !isNaN(lastChar)){
          display.value += operator;
        }
    }
     function appendDot() {
       var display = document.getElementById('display');
       if(!display.value.includes('.')){
        display.value += '.';
       }

     }
      
     function calculate() {
      var display =  document.getElementById('display');
      try{
        display.value = eval(display.value);
      }catch{
        display.value = "Error";
      }
     }
   

     //   var greeting =  "hi , My Name is  ";
     // var name = "Tee Godwin";
      //var joined = `${greeting}${name}`;
      //console.log(joined); 

      //var browserType = "Mozilla";
     // console.log(browserType)
     // how to replace the variabvle name that will be able to fit by using the replace method
     //var updated = browserType.replace("Van" , "Moz");
     // console.log(updated);
     // console.log(browserType);

     // to find the lenght of a string
  //   console.log(browserType.length);

        // Testing if a string contains a substring using include() startWith() and endWith()
   // if (browserType.includes("zilla")) {
    
    //console.log("Found Zilla")
   //}else{
    //console.log("No Zilla Found")
   //}
   //if(browserType.startsWith("Nilla")){
   //console.log("Found Nilla")
   //}
   //else{
    //console.log("No Nilla")
   //}
   // Finding the postion of a substring using the method called indeOf()
   //var into = "My name is Kehinde and I am a BlockChain Developer"
   //console.log(into.indexOf("JavaScript"));

 // Chaning to upper and lower case
 //ocnsole.log(into.toUpperCase());
 //console.log(into.tolowerCase());
