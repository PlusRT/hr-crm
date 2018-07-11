import React, { Component } from 'react';
import TextField from '@material-ui/core/TextField';
import { withStyles } from '@material-ui/core/styles';
import PropTypes from 'prop-types';

const styles = () => ({
    container: {
      display: 'flex',
      flexWrap: 'wrap',
    },
  });

class Input extends Component {
    render() {
        const { classes } = this.props;

        return(
            <div className={classes.container}>
                <TextField
                    id="full-width"
                    label={this.props.label}
                    placeholder={this.props.placeholder}
                    margin="normal"
                    name={this.props.name}
                    value={this.props.value}
                />
            </div>
        )
    }
}

Input.propTypes = {
    classes: PropTypes.object.isRequired
};

export default withStyles(styles)(Input);  