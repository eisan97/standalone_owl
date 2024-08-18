import {Component} from "@odoo/owl";
import {PrimaryButton} from "../buttons/primary_button/primary_button";

export class Root extends Component{
    static template = "standalone_owl.Root";
    static components = {PrimaryButton}
    static props = {};
}