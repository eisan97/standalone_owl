/** @odoo-module */

import {whenReady} from "@odoo/owl";
import {mountComponent} from "@web/env";
import {Root} from "./root/root"

whenReady(() => mountComponent(Root,document.body));