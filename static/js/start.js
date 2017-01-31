var MeinObj = null;

$(document).ready(function()
{    
function MeineApp(){
	var SessID = null;
	var Storage;
};
    
    MeineApp.prototype.SendeForm = function(){
        $.post('/login',$('#LArea').serialize()).done(function(data){
            if(data[0]){
            	MeinObj.SessID = data[1];
            	MeinObj.Storage.set('sid',data[1]);
                	
            	if(MeinObj.Storage.isSet('sid'))
            	{
            		window.location.href = '/backend';
            	}
            	
            	else {
            		$('#emsg').html('Please activate Cookies in your browser and retry.');
            	}                                                                        
            }
            
            else
            {
            	$('#emsg').html(data[1]);
            }                                                                       
        });
    };
    MeinObj = new MeineApp();
    MeinObj.Storage = Storages.cookieStorage;
    MeinObj.Storage.removeAll();
});