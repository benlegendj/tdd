    "use strict";
    module.exports={


    computeFactorial: (value) => {
        if (typeof(value) != 'number'){
            return "undefined";
        }

        else if  (value < 0)  {
            return "undefined";
        }
        else{
            let factorial=1;
            for (let counter=value;counter>=1;counter--){
                factorial=factorial*counter;
            }
            return factorial;
        }

   }
}
