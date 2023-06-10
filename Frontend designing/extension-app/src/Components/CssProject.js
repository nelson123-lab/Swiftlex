import React, {useState} from "react";
import Button from "@mui/material/Button";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";

const CssProject = () => {
  const [selectedText, setSelectedText] = useState("");
  const [open, setOpen] = useState(false);

  const handleSelection = () => {
    const selection = window.getSelection().toString();
    setSelectedText(selection);
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  return (
    <div onMouseUp={handleSelection}>
      <p>Select some text in this paragraph.</p>
      <p>Selected text: {selectedText}</p>
      {selectedText ? (
        <div style={{backgroundColor: "red"}}>
          <Dialog
            open={open}
            onClose={handleClose}
            aria-labelledby="alert-dialog-title"
            aria-describedby="alert-dialog-description"
          >
            <DialogActions>
              <Button onClick={handleClose}>Translate</Button>
              <Button onClick={handleClose}>Cancel</Button>
            </DialogActions>
          </Dialog>
        </div>
      ) : null}
    </div>
  );
};
export default CssProject;
