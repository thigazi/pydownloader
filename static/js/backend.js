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
    
    Backend.prototype.AddItem = function(cid){
                
    };
    
    Backend.prototype.DeleteItem = function(cid,iname){
        
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