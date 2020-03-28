function open_note(nid) {
    pycmd(`browser search:nid:${nid}`);
}
function add_nid_link(str) {
    return str.replace(/(\d{12,})/g, "<a onclick='open_note($1)'>$1</a>");
}

/* function from
 * https://stackoverflow.com/questions/298750/how-do-i-select-text-nodes-with-jquery*/
function getTextNodesIn(node, includeWhitespaceNodes) {
    var textNodes = [], nonWhitespaceMatcher = /\S/;

    function getTextNodes(node) {
        if (node.nodeType == 3) {
            if (includeWhitespaceNodes || nonWhitespaceMatcher.test(node.nodeValue)) {
                textNodes.push(node);
            }
        } else {
            for (var i = 0, len = node.childNodes.length; i < len; ++i) {
                getTextNodes(node.childNodes[i]);
            }
        }
    }

    getTextNodes(node);
    return textNodes;
}
