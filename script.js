function saveContent() {
    var title = document.getElementById('contentTitle').value;
    var body = document.getElementById('contentBody').value;

    var contentList = document.getElementById('contentList');
    var listItem = document.createElement('li');
    listItem.innerText = `Title: ${title}\nBody: ${body}`;
    contentList.appendChild(listItem);

    document.getElementById('contentTitle').value = '';
    document.getElementById('contentBody').value = '';
}
