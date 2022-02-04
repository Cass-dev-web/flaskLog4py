var templateDiv = `
<div><p style="text-align:left;">[dt]<span style="float:right; padding-right: 10px; color:[cl]">[st]</span></p><hr><textarea readonly>[da]</textarea></div><br>
`;
function timeout(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
var url = "consoles";
async function main(){
    while(true){
        var start_time = new Date().getTime();
        var req = $.get(url, function (data) { 
            var body = (document.querySelector("body").innerHTML)
            if(data!=""){
                reset = body != data
                if(reset==true){
                    document.querySelector("body").innerHTML= data
                }
            }else{
                document.querySelector("body").innerHTML='<p>Cannot find any consoles to display!</p><p class="small">If you think this is an error, report it at <a href="https://github.com/ParentProfanities/flaskLog4py/issues">our github</a>. This page will automatically change if it finds any consoles to display.</p>'
            }
            var request_time = new Date().getTime() - start_time;
            document.querySelector("head > title").innerHTML=`Took ${request_time/1000}s for request.`
        }); 
        req.error(function(jqXHR, textStatus, errorThrown) {
            if (textStatus == 'timeout')
                document.querySelector("body").innerHTML=`<p>Server timeout.</p>`

            if (textStatus == 'error')
                document.querySelector("body").innerHTML=`<p>Cannot find server!</p><p class="small">If you think this is an error, report it at <a href="https://github.com/ParentProfanities/flaskLog4py/issues">our github</a>. This page will automatically change if it finds any consoles to display.</p>`
                return

        });
        await timeout(delayTime)
    }
}
main()