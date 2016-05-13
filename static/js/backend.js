var BackendObj = null;
$(document).ready(function(){
    function Backend(){        
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
                                                            
                }
                
                else{
                    //session loeschen und zurueck
                }
            }
        });
    };
    
    Backend.prototype.DeleteItem = function(cid,iname){
        console.log(cid,iname);        
        $.get('/backend/code/'+cid+'?atype=deleteItem&fname='+iname,function(data){
                        
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