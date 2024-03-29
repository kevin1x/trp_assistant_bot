import React, { Component } from 'react';
import { connect } from 'react-redux';
import {
  Button,
  Form, FormGroup, ControlLabel, FormControl
} from 'react-bootstrap';
import CKEditor from "react-ckeditor-component";
import { Icon } from 'react-fa';

import * as actions from '../../actions';
import * as actionsTypes from '../../actions/types';
import * as API from '../../config/Api';
import * as ApiClient from '../../util/ApiClient';
import * as constants from '../../config/constant';
import * as Validater from '../../util/Validater';

class ModalAdd extends Component {

  constructor(props) {
    super(props);
    this.state = {
      dateFormat: 'DD/MM/YYYY',
      timeFormat: false,
      name: '',
      title: '',
      context: ''
    };
  }

  onChange = (event) => {
    this.setState({
      [event.target.id]: event.target.value
    });
  };

  changeValueTemplate = (newValue) => {
    this.setState({
      context: newValue
    });
  }

  clickClose = () => {
    this.props.toggleModal(false, actionsTypes.MAILTEMPLATE.TOGGLE_MODAL_ADD);
  };

  clickAdd = () => {
    const check = Validater.validateMailtemplate(this.state);
    if (!check.success) {
      alert(check.mess);
      return;
    }
    this.setState({
      isLoading: true
    });
    const {
      name, title, context
    } = this.state;
    ApiClient.addData(API.MAILTEMPLATES, { name, title, context })
    .then(res => {
      if (res.id) {
        ApiClient.getData(API.MAILTEMPLATES, actionsTypes.MAILTEMPLATE, constants.HAS_PREVIEW);      
        this.clickClose();
        alert("Thêm thành công");
        return;
      }
      const mes = Object.values(res).join('\n');
      alert(mes);
      this.setState({
        isLoading: false
      });
    })
    .catch(err => {
      alert("Có lỗi xuất hiện, vui lòng thử lại sau");
      this.setState({
        isLoading: false
      })
    });
  }

  render = () => {
    const {
      isLoading
    } = this.state;
    return (
      this.props.mailtemplate.showModalAdd ? 
      <div className="w3-modal show-modal">
        <div className="w3-modal-content clearfix">
          <div className="w3-container">
            <Form inline>
              <FormGroup> {/* Tên mẫu mail */}
                <ControlLabel>Thêm mẫu mail: </ControlLabel>
                <FormControl 
                  id="name"
                  type="text"
                  label="Text"
                  placeholder="Tên mẫu mail"
                  onChange={event => this.onChange(event)}
                />
                <ControlLabel>Tiêu đề: </ControlLabel>
                <FormControl 
                  id="title"
                  type="text"
                  label="Text"
                  placeholder="Tiêu đề"
                  onChange={event => this.onChange(event)}
                />
                <Button bsStyle="success" onClick={() => this.clickAdd()}>
                  { isLoading ? <Icon spin={true} name="circle-o-notch"/> : null } Thêm
                </Button>
                <Button onClick={() => this.clickClose()}>Hủy</Button>
              </FormGroup>
              <CKEditor 
                scriptUrl={constants.CKEDITOR_SCRIPT} 
                activeClass="p10" 
                onChange={this.changeValueTemplate.bind(this)} 
              />
            </Form>
          </div>
        </div>
      </div>
      : null
    );
  };
}

const mapStateToProps = (state, ownProps) => ({
  mailtemplate: state.mailtemplate,
});

const mapDispatchToProps = {
  toggleModal: actions.toggleModal,
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(ModalAdd);
