var BackendObj = null;
$(document).ready(function(){
    function Backend(){        
    };
    
    Backend.prototype.CheckSession = function(type){
    	$.get('/verify/session').done(function(data){
    		console.log(data);
    	});
    };
    
    Backend.prototype.Add = function(){
        $.get('/backend?atype=newkey',function(data){}).done(function(data){
            if(data[0]){
                if(data[1]){
                    window.location.href = '/backend/code/'+data[2];
                }
            }
            
            else{
                window.location.href = '/login';                
            }        
        });               
    };
    
    Backend.prototype.ChangeExpire = function(cid){
                        
    };
    
    Backend.prototype.AddItem = function(cid){        
        //data = [true,true,'MeineDatei'];
                             
        
        
        var fd = new FormData(document.forms.namedItem('ftsend'));
        fd.append("CustomField", "This is some extra data");
        $.ajax({
            url: "/backend/code/"+cid,
            type: "POST",
            dataType: "json",
            data: fd,
            processData: false,  // tell jQuery not to process the data
            contentType: false,   // tell jQuery not to set contentType
            success:function(data){
                if(data[0]){
                    if(data[1])
                    {
                        $($('table')[0].children[1]).append('<tr cid="'+data[2]+'"><td>'+data[2]+'</td><td>downloads &uuml;brig: <select><option value="0">0</option><option value="1">1</option><option value="2">2</option><option selected="selected" value="3">3</option><option value="4">4</option></select></td><td><img src="/img/delete.svg" onclick="BackendObj.DeleteItem(\''+cid+'\',\''+data[2]+'\');" width="20px" height="20"></td></tr>');
                        cn = parseInt($('#cfiles').html());
                        cn+=1;
                        $('#cfiles').html(cn); 
                    }
               }
            }
        });
    };
    
    Backend.prototype.DeleteItem = function(cid,iname){
        $.get('/backend/code/'+cid+'?atype=deleteItem&fname='+iname,function(data){
            if(data[0]){
                if(data[1]){
                    //It happens!
                    te = $('table')[0].children[1].children;
                    for(tx=0;tx<te.length;tx+=1){                        
                        if($(te[tx]).attr('cid')==data[2]){
                            $(te[tx]).remove();
                        }
                    }
                    
                    cn = parseInt($('#cfiles').html());
                    cn-=1;
                    $('#cfiles').html(cn);
                }
             }
             
             else{
                 //Session Expired!
             }
        });
              
    };
    
    Backend.prototype.DeleteALL = function(cid){
        $.get('/backend/code/'+cid+'?atype=deleteall',function(data){
            if(data[0]){
                //
                if(data[1]){
                    //console.log(data);
                    window.location.href = '/backend';                                        
                }
                
                else{                    
                }                                   
            }
            
            else{
                window.location.href = '/login';                
            }
        });      
    };
    
    Backend.prototype.Logout = function(){        
    };
    
    BackendObj = new Backend();    
});