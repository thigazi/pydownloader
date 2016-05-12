{% extends "backend.tpl" %}
{% block stuff %}
<b>Filelist</b><br>
Anzahl der Dateien in der DB: <b>{{dinfo.2}}</b>
<form accept-charset="UTF-8" style="margin-bottom: 10px;">
    <table>
        <thead>Download-Code: <b>{{cid.1}}</b></thead>
        <tbody>
            {% for dsx in dinfo.0%}            
            <tr><td>{{dsx}}</td><td>downloads &uuml;brig:
                <select>
                    {%for mxx in range(0,5)%}
                    <option value="{{mxx}}" {%if dinfo.1[dsx].maxtry == mxx %}selected="selected"{%endif%}>{{mxx}}</option>
                    {%endfor%}
                </select></td><td><img src="/img/delete.svg" width="20px" height="20"></td></tr>
            {%endfor%}            
        </tbody>
    </table>
    <form id="ftsend" name="ftsend" >
        <input type="file" name="ftsx" />
    </form>
</form>
<span><button onclick="BackendObj.DeleteALL('{{cid.1}}');">L&ouml;sche alles <b>KOMPLETT</b></button></span>
{% endblock %}