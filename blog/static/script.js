/* torna o menusinho clicável e aparente */
/* ter as tres opçoes dentro de um, faz com que eu possa alternar entre eles
   sem precisar fechar um, para depois abrir o outro */
let navbar = document.querySelector('.navbar');

document.querySelector('#menu-btn').onclick = () =>{
  navbar.classList.toggle('active'); 
  searchForm.classList.remove('active');
  cartItem.classList.remove('active');
}

/* torna o carrinho clicável */
let searchForm = document.querySelector('.search-form');

document.querySelector('#search-btn').onclick = () =>{
  searchForm.classList.toggle('active');
  navbar.classList.remove('active');
  cartItem.classList.remove('active');
}

/* torna a lupinha clicável */
let cartItem = document.querySelector('.cart-items-container');

document.querySelector('#cart-btn').onclick = () =>{
  cartItem.classList.toggle('active');
  navbar.classList.remove('active');
  searchForm.classList.remove('active');
}


window.onscroll = () =>{
  navbar.classList.remove('active');
  searchForm.classList.remove('active');
  cartItem.classList.remove('active');
}
