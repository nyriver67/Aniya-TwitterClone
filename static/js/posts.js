///////////////////////////
// JavaScript for Posts page
///////////////////////////

$(function() {
    // Executed when js-menu-icon js clicked
    $('.js-menu-icon').click(function() {
        //$(this) : self element, namely div.js-menu-icon
        //next() : next to div.js-menu-icon, namely div.menu
        //toggle() : switch show and hide
        $(this).next().toggle();
    })
})

/*const likeBtns = document.querySelectorAll('.like-btn');
likeBtns.forEach(btn => {
  btn.addEventListener('click', function() {
    const postId = this.dataset.postId;
    // send AJAX request to server to update likes table
    fetch('/like-post', {
      method: 'POST',
      body: JSON.stringify({ postId }),
      headers: {
        'Content-Type': 'application/json'
      }
      

    })
    .then(response => response.json())
    .then(data => {
      // update button appearance
      this.classList.add('liked');
      this.disabled = true;
      // update like count
      const likeCount = this.nextElementSibling;
      likeCount.textContent = data.likeCount;
    });
  });
});
*/

 