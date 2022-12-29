"use strict";

const buttons = document.querySelectorAll('a');
buttons.forEach((button) => {
    button.addEventListener('click', function (event) {

        const evenClassName = event.target.className;
        const childrenUl = document.querySelector(`a.${evenClassName} ~ ul`)

        if (childrenUl) {
            const allChildrenUl =  document.querySelectorAll(`ul.${childrenUl.classList[0]} ul`)

            childrenUl.classList.toggle('vis')
            if (!childrenUl.classList.contains('vis')) {
                 allChildrenUl.forEach((children) => {
                    children.classList.add('vis')
                });
            }
        }

    });
});