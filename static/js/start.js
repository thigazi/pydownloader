var MeinObj = null;

$(document).ready(function()
{    
function MeineApp(){};
    MeineApp.prototype.SendeForm = function(){
        $.post('/login',$('#LArea').serialize()).done(function(data){
            if(data[0] == true){
                try{
                    $.session.set('sid','sdsdsdsds');
                    if($.session.get('sid') != undefined){
                        //Bei Erfolg
                        window.location.href = '/backend';
                    }
                    
                    else{
                        
                        document.getElementById('emsg').innerHTML = 'Session abgelaufen';                        
                    }               
                }
                
                catch(err){
                    /*
                     *$('#emsg').innerHTML = 'Hallo Fehler!'; 
                     * funktionier nicht, warum auch immer....
                     */                    
                    //Cookies deaktiviert
                    document.getElementById('emsg').innerHTML = 'Bitte aktivieren Sie cookies und geben Sie das Passwort ein.<br>Neuladen der Webseite nicht notwendig';
                }                                                                           
            }
            
            else if(data[0] == false)
            {
                document.getElementById('emsg').innerHTML = data[1];                
            }                                                                       
        });
    };
    MeinObj = new MeineApp();        
});