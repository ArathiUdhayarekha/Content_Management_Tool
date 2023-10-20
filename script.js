function saveContent() {
    var title = document.getElementById('contentTitle').value;
    var body = document.getElementById('contentBody').value;
 if(title && body)
 {
    var contentList = document.getElementById('contentList');
    var listItem = document.createElement('li');
    listItem.innerText = `Title: ${title}\nBody: ${body}`;
    contentList.appendChild(listItem);
     clearEditor();
 }
 else{
        alter("please enter both title and content.");
     }
}
function clearEditor()
{
    document.getElementById('contentTitle').value = '';
    document.getElementById('contentBody').value = '';
}
