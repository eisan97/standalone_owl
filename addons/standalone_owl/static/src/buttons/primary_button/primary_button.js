/** @odoo-module */

import {Component} from "@odoo/owl";

export class PrimaryButton extends Component {
    static template = "standalone_owl.PrimaryButton";
    static components = {};
    // static props = {class: 'btn btn-primary'};
    static defaultProps = {
        class: 'btn bg-primary text-white m-5',
    };

    setup() {
        super.setup(...arguments);
        console.log(this.props);
    }
}