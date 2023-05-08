var iteration = ""

for(x = 97; x <= 122; x++){
    iteration = iteration + String.fromCharCode(x) + iteration;
    console.log(iteration);
}