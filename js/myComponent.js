import Vue from '../node_modules/vue/dist/vue.esm.browser.js';

export var myComponent = {
    template: `<span>
    This is a component and the value is {{x}}    

</span>`,
    props: ['x']
};

export default {}