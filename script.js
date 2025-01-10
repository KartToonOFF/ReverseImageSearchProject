const dropArea = document.getElementById('drop-area');
const fileInput = document.getElementById('file-input');
const placeholderIcon = 'file-placeholder.jpg';

// Empeche Google d'ouvrir l'image
function preventDefaults(e) {
  e.preventDefault();
  e.stopPropagation();
}

dropArea.addEventListener('dragover', preventDefaults);
dropArea.addEventListener('dragenter', preventDefaults);
dropArea.addEventListener('dragleave', preventDefaults);

// Script pour pouvoir glisser déposer les fichiers
dropArea.addEventListener('drop', handleDrop);

dropArea.addEventListener('dragover', () => {
  dropArea.classList.add('drag-over');
});

dropArea.addEventListener('dragleave', () => {
  dropArea.classList.remove('drag-over');
});

function handleDrop(e) {
  
  // Empeche Google d'ouvrir le fichier quand il est déposé  
  e.preventDefault();

  // Prend la liste des fichiers uploadés
  const files = e.dataTransfer.files;

  // Regarde si il y a un fichiers
  if (files.length) {
    // Assigne les fichiers a files
    fileInput.files = files;

    // Envoi les fichiers a la fonction handleFiles pour les afficher
    handleFiles(files);
  }
}

function handleFiles(files) {
  for (const file of files) {
    // Initialisation de l'affichage
    const reader = new FileReader();
    reader.readAsDataURL(file);

    // Quand le fichier est uploadé, lance l'affichage de l'image
    reader.onloadend = function (e) {
      const preview = document.createElement('img');
      
      // Affiche l'image si le type est valide, sinon affiche une icone par défaut
      if (isValidFileType(file)) {
        preview.src = e.target.result;
      } else {
        preview.src = placeholderIcon;
      }

      //Ajoute le CSS
      preview.classList.add('preview-image');
      const previewContainer = document.getElementById('preview-container');
      previewContainer.appendChild(preview);
    };
  }
}

function isValidFileType(file) {
  // Défini les types d'images autorisées
  const allowedTypes = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif'];
  return allowedTypes.includes(file.type);
}
