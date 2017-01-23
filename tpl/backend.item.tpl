{% extends "backend.tpl" %}
{% block stuff %}
<b>Filelist</b><br>
Anzahl der Dateien in der DB: <b id="cfiles">{{dinfo.2}}</b>

    <table>
        <thead>Download-Code: <b>{{cid.1}}</b></thead>
        <tbody>
            {% for dsx in dinfo.0%}            
            <tr cid="{{dsx}}"><td>{{dsx}}</td><td>downloads &uuml;brig:
                <select>
                    {%for mxx in range(0,5)%}
                    <option value="{{mxx}}" {%if dinfo.1[dsx].maxtry == mxx %}selected="selected"{%endif%}>{{mxx}}</option>
                    {%endfor%}
                </select></td><td><img src="/img/delete.svg" onclick="BackendObj.DeleteItem('{{cid.1}}','{{dsx}}');" width="20px" height="20"></td></tr>
            {%endfor%}            
        </tbody>
    </table>    
</form>
<form enctype="multipart/form-data" method="post" name="ftsend" id="ftsend">
    <input onchange="BackendObj.AddItem('{{cid.1}}');" id="ftupload" type="file" name="ftsx" />
    </form>
<span><button onclick="BackendObj.DeleteALL('{{cid.1}}');">L&ouml;sche alles <b>KOMPLETT</b></button></span>
{% endblock %}