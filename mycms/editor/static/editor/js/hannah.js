 
function makeChanges(form) {
    var nav_text1 = form.nav_link_1_text.value;
    var nav_text2 = form.nav_link_2_text.value;
    var nav_text3 = form.nav_link_3_text.value;
    var page_title = form.page_title.value;

    console.log(nav_text1)

    hannah_landing["nav-link-1-text"] = nav_text1;
    hannah_landing["nav-link-2-text"] = nav_text2;
    hannah_landing["nav-link-3-text"] = nav_text3;

    hannah_landing["page-title"] = page_title;

    console.log(hannah_landing)
}

