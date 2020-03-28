function add_link_reviewer() {
    if (_updatingQA) {
        setTimeout(function() {
            add_link_reviewer();
        }, 50);
        return;
    }
    $("#qa").each(function (idx, element) {
        text_nodes = getTextNodesIn(element, false);
        for (var i=0; i<text_nodes.length; i++) {
            node = text_nodes[i];
            $node = $(node)
            $node.replaceWith(add_nid_link(text_nodes[i].textContent));
        }
    });
}
