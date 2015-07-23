/**
 * Created by rikkt0r/grzegorz-wojcicki@outlook.com
 */

var Utils = (function(){

    return {
        cutToLength: function (text, len){
            if(text.length>len){
                return text.substring(0, len-3) + '...';
            } else {
                return text;
            }
        }
    }

})();